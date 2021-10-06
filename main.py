from argparse import ArgumentParser
from entities.user import User
from generator.user_generator import UserGenerator
from producer.user_producer import UserProducer


def parse_args():
    arg_parser = ArgumentParser()

    arg_parser.add_argument("--topic", required=False, default='user-test2', help='Topic Name')
    arg_parser.add_argument("--bootstrap-servers", required=False, default='VM IP',
                            help='Bootstrap server address')
    arg_parser.add_argument("--schema-registry", required=False, default='http://VM IP:8081',
                            help='Schema registry url')
    arg_parser.add_argument("--schema-file", required=False, default='create-user-request1.avsc',
                            help='File name of Avro schema')

    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    user_producer = UserProducer(args)
    user = User.generate_rand_user()
    for users in UserGenerator.generate():
        user_producer.send_records(users)
