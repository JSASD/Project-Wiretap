import argparse
import logging

def getArgs():
    # Initialize parser
    parser = argparse.ArgumentParser(description="Project Wiretap will systematically select extensions in rooms by building and wing using the Phantom algorithm")

    # Help prompts
    apiKeyPrompt = "Set API key to authenticate to GDMS with"

    # Add arguments
    parser.add_argument("-a", "--apikey", help = apiKeyPrompt, required=True)
    
    # Read arguments from command line
    args = parser.parse_args()

    # Create dictionary of arguments
    argValues = {
        'apiKey': args.apikey
    }

    logging.debug(argValues)
    return argValues