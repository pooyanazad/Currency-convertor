from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

API_KEY = '55555555555555555555555' #insert your real api 
API_URL = 'https://v6.exchangerate-api.com/v6/{}/latest/'.format(API_KEY)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Converter</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f3e5f5;
            color: #424242;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        .container {
            background-color: #e1bee7;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h2 {
            color: #6a1b9a;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input, select, button {
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            outline: none;
        }
        button {
            background-color: #ab47bc;
            color: white;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background-color: #9c27b0;
        }
    </style>
</head>
<body>
