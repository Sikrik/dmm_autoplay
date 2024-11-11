import gym

# 创建环境，指定渲染模式
env = gym.make("CartPole-v1", render_mode="human")

# 重置环境，获取初始观察和信息
observation, info = env.reset()

# 运行20步，测试环境
for _ in range(1000):
    # 渲染环境
    env.render()

    # 打印当前观察状态
    print(observation,f" reward is {info.get('reward')} ")

    # 随机选择一个动作
    action = env.action_space.sample()

    # 执行动作，获取新的观察、奖励、是否结束的标志和其他信息
    observation, reward, done, truncated, info = env.step(action)

    # 如果回合结束，重置环境
    if done or truncated:
        observation, info = env.reset()

# 关闭环境
env.close()