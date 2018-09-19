from DQN import DuelingDQNPrioritizedReplay
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import gym
from gym.wrappers import Monitor
import warnings

warnings.filterwarnings('ignore')

# env = gym.make('Breakout-ram-v0')
# env = env.unwrapped
#env = Monitor(env, "/tmp/",video_callable=lambda x: x % 100 == 0,force=True)

#print("Environment Built")

MEMORY_SIZE = 5000
ACTION_SPACE = 9
OBSERVATION_SPACE = 128

sess = tf.Session()
with tf.variable_scope('natural'):
    natural_DQN = DuelingDQNPrioritizedReplay(
        n_actions=ACTION_SPACE, n_features=OBSERVATION_SPACE, memory_size=MEMORY_SIZE,
        epsilon_increment=0.001, sess=sess, dueling=False,prioritized=False,
        output_graph=True)
    print("Natural DQN Built")


with tf.variable_scope('dueling'):
    dueling_DQN = DuelingDQNPrioritizedReplay(
        n_actions=ACTION_SPACE, n_features=OBSERVATION_SPACE, memory_size=MEMORY_SIZE,
        epsilon_increment=0.001, sess=sess, dueling=True, output_graph=True,
        prioritized=False)
    print("Dueling DQN Built")


with tf.variable_scope('PRmem'):
    prmem_DQN = DuelingDQNPrioritizedReplay(
        n_actions=ACTION_SPACE, n_features=OBSERVATION_SPACE, memory_size=MEMORY_SIZE,
        epsilon_increment=0.001, sess=sess, dueling=False, output_graph=True,
        prioritized=True)
    print("Prioritized Replay DQN Built")


with tf.variable_scope('duelingPRmem'):
    duelingPR_DQN = DuelingDQNPrioritizedReplay(
        n_actions=ACTION_SPACE, n_features=OBSERVATION_SPACE, memory_size=MEMORY_SIZE,
        epsilon_increment=0.001, sess=sess, dueling=True, prioritized=True,
        output_graph=True)
    print("Dueling DQN with Prioritized Replay Built")

sess.run(tf.global_variables_initializer())


def train(RL,directory):
    env = gym.make('MsPacman-ram-v0')
    env = Monitor(env, directory,video_callable=lambda count: count % 100 == 0,resume=True)
    acc_r = [0]
    total_steps = 0
    observation = env.reset()
    episodes= 0
    visualize = False
    while True:
        # if total_steps % 1000 == 0:
        #     print("total_steps = " + str(total_steps))
        if episodes % 100 == 0:
            visualize = True

        action = RL.pick_action(observation)

        f_action = action#(action-(ACTION_SPACE-1)/2)/((ACTION_SPACE-1)/4)   # [-2 ~ 2] float actions
        observation_, reward, done, info = env.step(np.array([f_action]))
        if visualize:
            env.render()

        #reward /= 10      # normalize to a range of (-1, 0)
        acc_r.append(reward + acc_r[-1])  # accumulated reward

        RL.store_trans(observation, action, reward, observation_)

        if total_steps > MEMORY_SIZE:
            RL.learn()

        if total_steps-MEMORY_SIZE > 45000:
            break

        if done:
            observation_= env.reset()
            episodes += 1
            visualize=False

        observation = observation_
        total_steps += 1
    print("Training Finished after {} episodes".format(str(episodes)))
    return RL.cost_history, acc_r

c_natural, r_natural = train(natural_DQN,"/tmp/natural/")
c_dueling, r_dueling = train(dueling_DQN,"/tmp/dueling/")
c_PRmem, r_PRmem = train(prmem_DQN,"/tmp/PRmem/")
c_duelingPR, r_duelingPR = train(duelingPR_DQN,"/tmp/duelingPR/")

plt.figure(1)
plt.plot(np.array(c_natural), c='r', label='natural')
plt.plot(np.array(c_dueling), c='b', label='dueling')
plt.plot(np.array(c_duelingPR), c='g', label='duelingPR')
plt.plot(np.array(c_PRmem), c='k', label='PRmem')
plt.legend(loc='best')
plt.ylabel('cost')
plt.xlabel('training steps')
plt.grid()

plt.figure(2)
plt.plot(np.array(r_natural), c='r', label='natural')
plt.plot(np.array(r_dueling), c='b', label='dueling')
plt.plot(np.array(r_duelingPR), c='g', label='duelingPR')
plt.plot(np.array(r_PRmem), c='k', label='PRmem')
plt.legend(loc='best')
plt.ylabel('accumulated reward')
plt.xlabel('training steps')
plt.grid()

plt.show()
