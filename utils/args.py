import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-name", default="ALE/Breakout-v5")
    parser.add_argument("--render-mode", choices=["rgb_array", "human"], default="rgb_array")
    parser.add_argument("--seed", type=int, default=36)
    parser.add_argument("--max-episodes", type=int, default=10)
    parser.add_argument("--max-steps-per-episode", type=int, default=10000) 
    parser.add_argument("--policy", choices=["random", "dqn",], default="random")
    parser.add_argument("--render-fps", type=int, default=10)
    parser.add_argument("--output-video-path", default="output.mp4")

    return parser.parse_args()