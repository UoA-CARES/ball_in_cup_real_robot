import os
import json
import urx
import logging
logging.basicConfig(level=logging.INFO)
import collections
collections.Iterable = collections.abc.Iterable # Need this for math3d lib issues

from environment.main_environment_ur5 import Environment



def read_config_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config', 'robot_config.json')
    with open(config_path) as f:
        config = json.load(f)
    return config

def read_camera_files():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config')
    camera_matrix = config_path + '/matrix.txt'
    camera_distortion = config_path + '/distortion.txt'
    return camera_matrix, camera_distortion


def main():
    config = read_config_file()
    camera_matrix, camera_distortion = read_camera_files()
    ip_address_robot = config['ip_robot']

    # robot = urx.Robot(ip_address_robot, use_rt=True, urFirm=config['urFirm'])
    robot = urx.Robot(ip_address_robot)

    env = Environment(robot,
                      velocity=config['velocity'],
                      acceleration=config['acceleration'],
                      camera_matrix=camera_matrix,
                      camera_distortion=camera_distortion)


    env.starting_position()  # just making sure the joint are in the right position for initialization
    env.robot_home_position()

    while True:
        env.get_state()

    # for i in range(10):
    #     env.hard_code_solution()
    #     env.reset_task()
    # env.robot_home_position()

    robot.close()


if __name__ == "__main__":
    main()


