query = """
{
    product {
        price(number only, without the currency)
        currency
        color
        version
    }
    
    distributor {
        name
        absolute_url
    }
    
    product_reviews[] {
        author
        stars
        content
        attachments[] {
            absolute_url
        }
        color
        version
        date
        location
        upvote_number
    }
}
""".strip()


class JdComments:
    def __init__(self):
        pass

    def get_comments(self):
        return "Comments"

    def get_comments_by_page(self, page):
        return "Comments by page"

if __name__ == "__main__":
    print("Hello, World!")

