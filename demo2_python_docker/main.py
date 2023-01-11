import logging
import random

choice = ["❤️", "🐋", "😈", "😍"]

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def main():

    return random.choice(choice)

if __name__ == "__main__":
    
    icon = main()
    
    log.info(f"Hello from Docker, Docker is {icon}")

