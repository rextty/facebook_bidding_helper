from Model import facebook_api


class Bidding:
    def __init__(self):
        self.__FacebookAPI = facebook_api.FacebookAPI("883121082969101", "token...")

    def check_bidding(self, post_id):
        comments = self.__FacebookAPI.get_post_comment(post_id)
        print(comments)
        for comment in comments["data"]:
            print(comment["message"])

        # Has next
        if comments["paging"]["next"]:
            pass


if __name__ == "__main__":
    obj = Bidding()
    # obj.check_bidding("883121082969101_883146332966576")
    obj.check_bidding("883121082969101_883146386299904")
