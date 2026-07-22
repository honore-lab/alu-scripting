#!/usr/bin/python3
import importlib

top_ten = importlib.import_module("api_advanced.1-top_ten").top_ten

print("--- Testing Python Subreddit ---")
top_ten("python")

print("--- Testing Fake Subreddit ---")
top_ten("this_is_a_fake_subreddit_12345")
