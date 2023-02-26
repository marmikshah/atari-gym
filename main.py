import cv2
import gymnasium as gym

from utils.args import get_args
from policies.base import RandomPolicy
from utils.imtools import create_reset_frame


def main():
    args = get_args()
    env = gym.make(args.env_name, render_mode=args.render_mode)
    env.metadata['render_fps'] = args.render_fps

    cap = None

    policy = RandomPolicy(env.action_space)

    height, width = None, None

    for episode in range(args.max_episodes):
        print("Episode:", episode)
        observation, info = env.reset(seed=args.seed)
        if cap is None:
            frame = env.render()
            height, width, _ = frame.shape
            cap = cv2.VideoWriter(args.output_video_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 10, (width, height))

        for _ in range(args.max_steps_per_episode):
            frame = env.render()
            cap.write(frame)
            action = policy.step(observation, frame)
            observation, reward, terminated, truncated, info = env.step(action)

            if terminated or truncated:
                break
        
        frame = create_reset_frame(width, height)
        for _ in range(args.render_fps):
            cap.write(frame)
    cap.release()


if __name__ == "__main__":
    main()
