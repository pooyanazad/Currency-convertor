from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = '55555555555555555555555' #insert your real api 
API_URL = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format(API_KEY)
