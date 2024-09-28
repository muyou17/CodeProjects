from time import sleep
from ballyregan.core.exceptions import NoInternetConnection, ProxyException
from poe_api_wrapper import PoeApi


def get_tokens() -> dict[str, str]:
    tokens = {}
    with open('tokens.txt', 'r') as file:
        try:
            tokens['p-b'], tokens['p-lat'] = file.read().splitlines()
            if len(tokens['p-b']) > len(tokens['p-lat']):
                raise ValueError("p-b must be shorter than p-lat")
        except Exception as exception:
            print(f"Error: {exception}")
            print("Exiting…"); sleep(5)
    return tokens


def create_client(tokens: dict[str, str]) -> PoeApi:
    try:
        return PoeApi(tokens)
    except Exception as exception:
        print(f"Error: {exception}\nYour tokens are probably wrong.")
        print("Exiting…"); sleep(5)


def find_bot(client: PoeApi) -> str:
    models = ('gpt4_o', 'gpt4_o_mini_128k', 'gpt4_o_mini', 'claude_3_igloo_200k', 'claude_3_igloo', 'acouchy',
              'chinchilla', 'claude_2_1_bamboo', 'claude_3_haiku_200k', 'claude_3_haiku', 'capybara', 'a2_100k',
              'a2', 'gpt3_5', 'gemini_pro_search', 'chinchilla_instruct', 'code_llama_34b_instruct',
              'code_llama_13b_instruct', 'upstage_solar_0_70b_16bit')
    message = "Hi! I want to practice my English right now, chat with me!"
    for bot in models:
        try:
            client.send_message(bot, message)
            return bot
        except RuntimeError as exception:
            print(f"{bot} is unusable: {exception}\nFinding another bot…")
    else:
        print("Couldn't find any bot.")
        print("Exiting…"); sleep(5)


def main() -> None:
    client = create_client(get_tokens())
    bot = find_bot(client)


if __name__ == '__main__':
    main()