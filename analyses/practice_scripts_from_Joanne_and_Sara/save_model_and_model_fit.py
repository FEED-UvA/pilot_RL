    def fit_RL_stan_EBR(self, ebr_data, ebr_label, model_name = 'stan_RL_train_precision', 
                        iterations=2000, chains=4, run_model=False):
        """run RL model for high and low blinkers to assess their learning rates and explore-exploit tendencies """

        #n_s        = number of subjects 
        #n_t        = number of trials 
        #correct    = correct response; 1=correct/2=incorrect
        #reward     = rewarded response;0=no reward/1=reward
        #cur_stim   = presented stimuli per trial
        #init_sj    = marks start of a new subject 
        #subject    = mapping between trial and subject nr 

        #import stan model 
        stan_model_code = stan_model.import_stan_model_code()

        #behavioural data train phase 
        df_train_sjs = self.gather_dataframes_from_hdfs(group = 'train_behaviour', data_type = 'df_train_all') 
        #trials within response time window 
        valid = [np.array(~df_train_sjs[s]['ommissions']) for s in range(len(self.sessions))]

        ebr = self.get_ebr(ebr_data)

        #split subjects based on median ebr 
        if ebr_label == 'low': 
            ebr_sjs = [i for i,val in enumerate(ebr) if val < np.median(ebr)]
        else: 
            ebr_sjs = [i for i,val in enumerate(ebr) if val > np.median(ebr)]

        #fit data of ebr_label group 
        n_s = len(ebr_sjs)
        n_t = [sum(valid[s]) for s in ebr_sjs]
        total_n_t = np.sum(n_t)

        #concatenate relevant behavioural data across ebr_label subjects 
        correct = np.concatenate([np.array(df_train_sjs[s]['correct_STAN'][valid[s]]) for s in ebr_sjs])
        reward = np.concatenate([np.array(df_train_sjs[s]['rewarded']).astype(int)[valid[s]] for s in ebr_sjs])
        cur_stim = np.concatenate([np.array(df_train_sjs[s]['cur_stim'][valid[s]]) for s in ebr_sjs])
        init_sj = np.concatenate([np.r_[1, np.zeros(n_t[s])][:-1].astype(int) for s in range(len(ebr_sjs))])
        subject = np.concatenate([np.repeat(s+1, n_t[s]) for s in range(len(ebr_sjs))])

        #recode cur_stim into 1,3,5 to sync with STAN 
        cur_stim = self.recode_stim_for_STAN(cur_stim)
   
        #data to feed into the model
        stan_data = {'n_s': n_s, 'n_t': total_n_t, 'Choice': cur_stim, 'Correct': correct, 
                    'Reward': reward, 'Init': init_sj, 'Subject': subject}
        print(ebr_label + ' ebr subjects: ', stan_data)


        model_pkl = os.path.join(self.grouplvl_data_dir, 'EBR_paper', 'models',  'model_%s.pkl')%model_name   
        #model + fit dir        
        model_fit_pkl = os.path.join(self.grouplvl_data_dir, 'EBR_paper', 'model_fits', '%s_%s_%s_IT%i_CH%i_N%i.pkl')\
        %(ebr_label, ebr_data, model_name, iterations, chains, len(ebr_sjs))        

        #check if model is already compiled 
        check = os.path.isfile(model_pkl)   
        if check == False:  
            sm = pystan.StanModel(model_code=stan_model_code, model_name=model_name) #compile model          
            #save model 
            with open(model_pkl, 'wb') as f:
                pickle.dump(sm, f)
        else:
            with open(model_pkl, 'rb') as f: 
                sm = pickle.load(f)

        #run model
        if run_model: 
            fit = sm.sampling(data=stan_data, chains=chains, iter=iterations, 
                                init='random', n_jobs=-1)   

            #save model + samples
            with open(model_fit_pkl, "wb") as f:
                pickle.dump({'model' : sm, 'fit' : fit}, f, protocol=-1)
        
        #load model 
        else: 
            #load samples 
            with open(model_fit_pkl, "rb") as f:
                data_dict = pickle.load(f)
            fit = data_dict['fit']  