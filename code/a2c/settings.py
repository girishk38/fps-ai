import os

# disable tensorflow debugging
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

RESOLUTION = [30, 45]

DEFAULT_GAME = "Vizdoom"
MAX_EPISODES = 3000
NUM_STEPS = 300
GAMMA = 0.95
HIDDEN_SIZE = 6

UPDATES = 1000
BATCH_SIZE = 64

# BASE_DIR = parent directory of code directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuration file path
DEFAULT_MODEL_SAVEFILE = "tmp/a2c/model-{}.tf"
DEFAULT_CONFIG = "config/basic.cfg"