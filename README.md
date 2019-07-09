# earl302.py
## The Earl of Redirect Services

earl302 is a redirect service written in Python.
What makes earl302 unique is that users do not have
to create the shortened URL prior to using it. Instead
earl302 uses base64 encoding to determine where to
redirect a URL. What this means is that all you have to do
is encode a URL with base64.

While earl302 can't get URLs as short as other URL redirect
services can, for the discerning user this might be worth
it, as earl302 doesn't have any mechanism for collecting
user data. With a lot of these url redirect services the
trade off is they can and often will collect your data and
then turn that over to whoever created the shortened URL.
But because no one can "create" a shortened URL with earl302,
there is no ability to collect and pass on the data.

## Usage
If you want to test out earl302, it's pretty easy to do!

1. clone it
2. install flask
> `pip install flask`
3. start earl302.py
> `FLASK_APP=earl302.py flask run`
4. Profit!

Once it's running try testing it in your terminal with:
`curl -L "127.0.0.1:5000/$(echo 'google.com' | base64)"`

You should, hopefully, get an ungodly mess of HTML right
from your neighborhood, NSA-funded datacenter!
