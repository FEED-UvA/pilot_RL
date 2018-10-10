#!/usr/bin/env python
# encoding: utf-8

def import_stan_model_code(): 

	stan_model = """

	data{
	  int<lower=1> n_s;                       // total number of subjects
	  int<lower=1> n_t;                       // total number of trials (summed across all subjects)
	  int<lower=1,upper=5> Choice[n_t];       // choice option, trial n_t (choice is 1,3 or 5). (All subjects stacked)
	  int<lower=1,upper=2> Correct[n_t];      // correct=1, incorrect=2, trial n_t
	  int<lower=0,upper=1> Reward[n_t];       // reward=1, no reward =0, trial n_t
	  int<lower=1,upper=n_s> Subject[n_t];    // subject number n_s, trial n_t 
	  int<lower=0,upper=1> Init[n_t];         // initialize new subject (1 = new init), trial n_t
	}                                         // end data 
	  

	parameters{
	  // group level mean parameters
		real mu_b_pr; 				  //inverse gain parameter
		real mu_ag_pr;   				//alphaG
		real mu_al_pr;   				//alphaL
	 

	  // group level standard deviation
	  real<lower=0> sd_b;   			  //inverse gain parameter
		real<lower=0> sd_ag;   				//alphaG
		real<lower=0> sd_al;   				//alphaL
	  

	  // individual level parameters
	  real b_ind_pr[n_s];   			  //inverse gain parameter
		real ag_ind_pr[n_s];   				//alphaG
		real al_ind_pr[n_s];   				//alphaL
		}//end paramters
		
	transformed parameters{
		// group level mean parameters
	  real<lower=0,upper=100> mu_b; 				//inverse gain parameter
		real<lower=0,upper=1> mu_ag;   				//alphaG
		real<lower=0,upper=1> mu_al;   				//alphaL
	 

	  // individual level parameters
	  real<lower=0,upper=100> b_ind[n_s];     		//inverse gain parameter
		real<lower=0,upper=1> ag_ind[n_s];   				//alphaG
		real<lower=0,upper=1> al_ind[n_s];   				//alphaL
	 

	  // group level mean parameters (probit)
	  mu_b  =Phi(mu_b_pr)*100;   		//inverse gain parameter
		mu_ag =Phi(mu_ag_pr);   				//alphaG
		mu_al =Phi(mu_al_pr);   				//alphaL
	  

	  // individual level parameters (probit)
	  for (s in 1:n_s)
	  {
	    b_ind[s]  = Phi(b_ind_pr[s])*100;
	    ag_ind[s] = Phi(ag_ind_pr[s]);
	    al_ind[s] = Phi(al_ind_pr[s]);
	    
	  }// end for loop
	  
		}// end transformed parameters
		


	model{
	  // define general variables needed for subject loop
	  int si;
	  real prQ0[6];
	  real prQ[6];
	  real Qchoice[2];
	  real epsilon;
	  int a;
	  real alpha;
	  vector[2] pchoice;

	  // set prior on group level mean parameters
	  mu_b_pr ~  normal(0,1);   			  //inverse gain parameter
		mu_ag_pr ~ normal(0,1);   				//alphaG
		mu_al_pr ~ normal(0,1);   				//alphaL
	 

	  // set prior on group level standard deviations
	  sd_b ~  uniform(0,1.5);     		  //inverse gain parameter
		sd_ag ~ uniform(0,1.5);   				//alphaG
		sd_al ~ uniform(0,1.5);   				//alphaL
	  

	  // set prior for individual level parameters
	  for (s in 1:n_s)
	  {
	    b_ind_pr[s] ~ normal(mu_b_pr,   sd_b);     		    //inverse gain parameter
		  ag_ind_pr[s]~ normal(mu_ag_pr,  sd_ag);   				//alphaG
		  al_ind_pr[s]~ normal(mu_al_pr,  sd_al);   				//alphaL
	   
	  }

	  
	  
	  // defineer epsilon
	  epsilon = 0.00001;

	  // now start looping over subjects
	  for (t in 1:n_t)
	  {

	      // set initial values subject
	      if (Init[t]==1){
	            si= Subject[t];
	            for (v in 1:6)
	              {
	                prQ0[v] = 0.5;
	                prQ[v] = 0.5;

	              }// end inital values loop
	          // trial 1
	          pchoice[1]=0.5;
	          pchoice[2]=0.5;
	        }

	   
	          Qchoice[1]    = prQ[Choice[t]]; 
	          Qchoice[2]    = prQ[(Choice[t]+1)];
	            pchoice[1]    = 1/(1+exp(b_ind[si]*(Qchoice[2]-Qchoice[1])));
	                pchoice[2]    = 1-pchoice[1];
	                pchoice[1]    = epsilon/2+(1-epsilon)*pchoice[1];
	          pchoice[2]    = epsilon/2+(1-epsilon)*pchoice[2];

	          Correct[t]~categorical(pchoice);
	          a = Correct[t]-1; //0=correct,1=incorrect	

	                // reinforcement
	          alpha = Reward[t]*ag_ind[si]+(1-Reward[t])*al_ind[si];
	                prQ[(Choice[t]+a)] = prQ[(Choice[t]+a)] + alpha*(Reward[t]-prQ[(Choice[t]+a)]);

	 
	   }// end subject loop
	}// end of model loop

	"""
	return stan_model


def import_updated_stan_model_code(): 
	""" update of import_stan_model_code(), 
	adjustments:
	- Phi_approx() replaces Phi() for probit transform 
	- prior on group-level changed from uniform(0,1.5) to cauchly(0,5)
	- prior on individual-level parameters not determined by prior on group-level parameters
	- returns single-trial RPE, Qchosen, Qunchosen, RPE_update en Qchosen_update variables, next 
	to fitted group-level and individuel-level posterior distribututions.

	"""
	stan_model = """

	data{
	  int<lower=1> n_s;                       // total number of subjects
	  int<lower=1> n_t;                       // total number of trials (summed over all subjects)
	  int<lower=1,upper=5> Choice[n_t];       // choice option, trial n_t (choice is 1,3 of 5). (All subjects stacked)
	  int<lower=1,upper=2> Correct[n_t];      // correct=1, incorrect=2, trial n_t
	  int<lower=0,upper=1> Reward[n_t];       // reward=1, no reward =0, trial n_t
	  int<lower=1,upper=n_s> Subject[n_t];    // subject number n_s, trial n_t 
	  int<lower=0,upper=1> Init[n_t];         // initialize new subject (1 = new init), trial n_t
	}                                         // end data 	  

	parameters{
	  // group level mean parameters
		real mu_b_pr; 				  	//inverse gain parameter
		real mu_ag_pr;   				//alphaG
		real mu_al_pr;   				//alphaL
	 

	  // group level standard deviation
	  	real<lower=0> sd_b;   			  	//inverse gain parameter
		real<lower=0> sd_ag;   				//alphaG
		real<lower=0> sd_al;   				//alphaL
	  

	  // individual level parameters
	  	real b_ind_pr[n_s];   			  	//inverse gain parameter
		real ag_ind_pr[n_s];   				//alphaG
		real al_ind_pr[n_s];   				//alphaL
		}//end paramters
		


	transformed parameters{
	  // group level mean parameters
	  	real<lower=0,upper=100> mu_b; 				//inverse gain parameter
		real<lower=0,upper=1> mu_ag;   				//alphaG
		real<lower=0,upper=1> mu_al;   				//alphaL
	 

	  // individual level parameters
	  	real<lower=0,upper=100> b_ind[n_s];     			//inverse gain parameter
		real<lower=0,upper=1> ag_ind[n_s];   				//alphaG
		real<lower=0,upper=1> al_ind[n_s];   				//alphaL
	 

	  // group level mean parameters (probit)
	  	mu_b  =Phi_approx(mu_b_pr)*100;   			//inverse gain parameter
		mu_ag =Phi_approx(mu_ag_pr);   				//alphaG
		mu_al =Phi_approx(mu_al_pr);   				//alphaL
	  

	  // individual level parameters (probit)
	  for (s in 1:n_s)
	  {
	    b_ind[s]  = Phi_approx(mu_b_pr + sd_b * b_ind_pr[s]) * 100;
	    ag_ind[s] = Phi_approx(mu_ag_pr + sd_ag * ag_ind_pr[s]);
	    al_ind[s] = Phi_approx(mu_al_pr + sd_al * al_ind_pr[s]);
	    
	  }// end for loop
	  
		}// end transformed parameters
		


	model{
	  // define general variables needed for subject loop
	  int si;
	  real prQ0[6];
	  real prQ[6];
	  real Qchoice[2];
	  real epsilon;
	  int a;
	  real alpha;
	  vector[2] pchoice;
	  // defineer epsilon
	  epsilon = 0.00001;


	  // set prior on group level mean parameters
	  	mu_b_pr ~  normal(0,1);   			  	//inverse gain parameter
		mu_ag_pr ~ normal(0,1);   				//alphaG
		mu_al_pr ~ normal(0,1);   				//alphaL
	 

	  // set prior on group level standard deviations
	  	sd_b ~  cauchy(0, 5);     		  	//inverse gain parameter
		sd_ag ~ cauchy(0, 5);   			//alphaG
		sd_al ~ cauchy(0, 5);  				//alphaL
	  

	  // set prior for individual level parameters
	  for (s in 1:n_s)
	  {
	   	  b_ind_pr[s] ~ normal(0, 1);     		    	//inverse gain parameter
		  ag_ind_pr[s]~ normal(0, 1);   				//alphaG
		  al_ind_pr[s]~ normal(0, 1);   				//alphaL
	   
	  }

	  

	  // now start looping over subjects
	  for (t in 1:n_t)
	  {

	      // set initial values subject
	      if (Init[t]==1){
	            si= Subject[t];
	            for (v in 1:6)
	              {
	                prQ0[v] = 0.5;
	                prQ[v] = 0.5;

	              }// end inital values loop
	          // trial 1
	          pchoice[1]=0.5;
	          pchoice[2]=0.5;
	        }

	   
	          Qchoice[1]    = prQ[Choice[t]]; 
	          Qchoice[2]    = prQ[(Choice[t]+1)];
	          pchoice[1]    = 1/(1+exp(b_ind[si]*(Qchoice[2]-Qchoice[1])));
	          pchoice[2]    = 1-pchoice[1];
	          pchoice[1]    = epsilon/2+(1-epsilon)*pchoice[1];
	          pchoice[2]    = epsilon/2+(1-epsilon)*pchoice[2];

	          Correct[t]~categorical(pchoice);
	          a = Correct[t]-1; //0=correct,1=incorrect	

	          // reinforcement
	          alpha = Reward[t]*ag_ind[si]+(1-Reward[t])*al_ind[si];
	          prQ[(Choice[t]+a)] += alpha*(Reward[t]-prQ[(Choice[t]+a)]);

	 
	   }// end subject loop
	}// end of model loop



	generated_quantities{

	  // See Github code from Ahn Young for similar setup : https://github.com/youngahn/hBayesDM/blob/master/exec/prl_rp.stan 
	  
	  real log_lik[n_s];        // For log likelihood calculation (on a per subject basis)
	  real RPE[n_t];            // For reward prediction error calculation (on a subject and per-trial basis)
	  real Qval_chosen[n_t];    // For cue-value of chosen stimulus
	  real Qval_unchosen[n_t];  // For cue-value of unchosen stimulus

	  real Qval_update[n_t];    // For updated Q-value of chosen stimulus
	  real RPE_update[n_t];     // For the weighted RPE update of chosen stimulus
	  // For posterior predictive check
	  real y_pred[n_t];

	  { // local section, saves time and space

	    // Setting up variables for trial-to-trial modelling, log_lik and RPE calculations.
	    int si;
	    real prQ0[6];
	    real prQ[6];
	    real Qchoice[2];
	    real epsilon;
	    int a;
	    int b;
	    real alpha;
	    vector[2] pchoice;
	    epsilon = 0.00001;
	    
	    for (t in 1:n_t) {

	      // Almost the same setup as in model{} block, just with log_lik and RPE calculations added (& trial-to-trial regressors for Q-values).

	      if (Init[t]==1){
	        si= Subject[t];
	        for (v in 1:6)
	        {
	          prQ0[v] = 0.5;
	          prQ[v] = 0.5;

	        }// end inital values 

	        // trial 1
	        pchoice[1]=0.5;
	        pchoice[2]=0.5;

	        # Initialise log_lik to 0 for each participant        
	        log_lik[si] = 0;
	      }


	          Qchoice[1]    = prQ[Choice[t]]; 
	          Qchoice[2]    = prQ[(Choice[t]+1)];
	          pchoice[1]    = 1/(1+exp(b_ind[si]*(Qchoice[2]-Qchoice[1])));
	          pchoice[2]    = 1-pchoice[1];
	          pchoice[1]    = epsilon/2+(1-epsilon)*pchoice[1];
	          pchoice[2]    = epsilon/2+(1-epsilon)*pchoice[2];


	      // Log likelihood of the softmax choice. Gets updated on the subject level, given trial-to-trial choices.
	      log_lik[si] += categorical_lpmf( Correct[t] | pchoice);
	      y_pred[t] = categorical_rng(pchoice);

	      a = Correct[t]-1; //  0=correct,1=incorrect	
	      b = abs(a-1); 	//  ifloops are very slow in stan
	      
	      // Model regressors - store values before being updated

	      RPE[t] =  Reward[t]-prQ[(Choice[t]+a)];  // Reward prediction error
	      Qval_chosen[t] = prQ[(Choice[t]+a)];     // Q-value chosen stimulus
	      Qval_unchosen[t] = prQ[(Choice[t]+b)];   // Q-value unchosen stimulus


	      // Reinforcement - update Q-values based on current outcome
	      alpha = Reward[t]*ag_ind[si]+(1-Reward[t])*al_ind[si];
	      prQ[(Choice[t]+a)] += alpha*(Reward[t]-prQ[(Choice[t]+a)]);

	      Qval_update[t] = prQ[(Choice[t]+a)];
	      RPE_update[t] = alpha * (Reward[t]-prQ[(Choice[t]+a)]);

	   }
	  }  
	}
	"""

	return stan_model

