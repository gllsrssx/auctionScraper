from flask import Flask, render_template, request
import json
import multiprocessing
import scraper
import update
 
app = Flask(__name__)
data_results = update.main()
cars_per_page = 25

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    start_idx = (page - 1) * cars_per_page
    end_idx = start_idx + cars_per_page
    current_page_cars = data_results[start_idx:end_idx]
    total_pages = (len(data_results) + cars_per_page - 1) // cars_per_page
    has_more_pages = end_idx < len(data_results)
    
    data_to_send = {
        'cars_per_page': cars_per_page, 
        'amount_of_cars': len(data_results),
        'cars': current_page_cars,
        'has_more_pages': has_more_pages,
        'page': page,
        'total_pages': total_pages,
    }

    return render_template('index.html', data=data_to_send)

if __name__ == '__main__':
    app.run()
