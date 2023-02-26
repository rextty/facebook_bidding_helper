import requests
import re


class FacebookAPI:
    def __init__(self, group_id, api_token):
        host = "https://graph.facebook.com"
        version = "v16.0"
        self.__api_url = f"{host}/{version}"
        self.__group_id = group_id
        self.__api_token = api_token

    def __get_url(self, first_parameter) -> str:
        """
        __get_url just format the api url, I don't know there is have a better way or not.
        :param first_parameter: put at url middle.
        :return: formatted api uri.
        """
        return f"{self.__api_url}/{first_parameter}?access_token={self.__api_token}"

    def get_all_posts(self) -> str:
        """
        get_all_posts get all post of groups
        :return:
        """
        url = self.__get_url(f"{self.__group_id}/feed")
        rs = requests.get(url)
        return rs.json()

    def get_post_comment(self, post_id) -> str:
        """
        get_post_comment get comments of post
        :param post_id:
        :return:
        """
        url = self.__get_url(f"{post_id}/comments")
        rs = requests.get(url)
        return rs.json()

    def get_short_access_token(self):
        url = "https://graph.facebook.com/oauth/access_token" \
               "?client_id=" \
               "&client_secret=" \
               "&grant_type=client_credentials"
        rs = requests.get(url)
        json_rs = rs.json()
        if json_rs["access_token"]:
            result = re.search("(?<=\|).*", json_rs["access_token"])
            if result:
                return result[0]

    def get_long_access_token(self):

        url = "https://graph.facebook.com/v16.0/oauth/access_token?" \
              "grant_type=fb_exchange_token&" \
              "client_id=&" \
              "client_secret=&" \
              "fb_exchange_token="
        rs = requests.get(url)
        print(rs.json())


if __name__ == "__main__":
    # Testing
    obj = FacebookAPI("883121082969101", "token...")
    # obj.get_all_posts()
    # obj.get_post_comment("883121082969101_883146332966576")
    obj.get_short_access_token()
