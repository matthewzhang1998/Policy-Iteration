import numpy as np

def initialize_prob():
    # Define the probability associated with each state-action-state transition
    pass

def initialize_reward():
    # Define the reward associated with each state-action-state transition
    pass

# performs an update on the value matrix
def bellman_update():
    for s in range(number_states):
        value_matrix[s] =  np.dot(np.transpose(prob_matrix[s, policy[s],:]),(reward_matrix[s, policy[s],:] + gamma * value_matrix[:]))

# performs an update on the policy
def policy_update():
    for s in range(number_states):
        Q_best = value_matrix[s]
        # print "State", s, "q_best", q_best
        for a in range(number_actions): 
            Q_value = np.dot(np.transpose(prob_matrix[s, a,:]),(reward_matrix[s, a,:] + gamma * value_matrix[:]))
            if Q_value > Q_best:
                policy[s] = a
                Q_best = Q_value

if __name__ == "__main__":
    states = [] # populate with states
    actions = [] # populate with actions
    number_states = len(states)
    number_actions = len(actions)
    prob_matrix = np.zeros((number_states, number_actions, number_states))
    reward_matrix = np.zeros((number_states, number_actions, number_states))
    
    # initialize policy and value arbitrarily
    value_matrix = np.zeros(number_states)
    policy = []
    for s in range(number_states):
        policy.append(0)
        
    gamma = 0.
        
    initialize_prob()
    initialize_reward()

    iterations = 1000 # Iteratively update value matrix and policy
    for i in range(iterations):
        bellman_update()
        policy_update()