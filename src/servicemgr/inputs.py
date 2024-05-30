import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Service Manager')
    parser.add_argument('COMMAND', type=str, help='Type your command')
    parser.add_argument('--telegram-bot-id', '-tb', type=str, help='id of telegram bot')
    parser.add_argument('--telegram-group-id', '-tg', type=str, help='id of telegram group')
    parser.add_argument('--data-dir', '-d', type=str, help='Where data store.', default='~/.servicemgr')
    parser.add_argument('--service-name', '-s', type=str, help='Name of service')
    parser.add_argument('--max-service-breaktime', '-mb', type=int, help='Maximum break time of service (seconds)')
    parser.add_argument('--listener', '-l', type='str', help='Listener host and port. Example: localhost:5644')
    return parser.parse_args()
