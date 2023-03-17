from typing import List 

from fastapi import FastAPI, APIRouter

import db, schema

# flask_app = Flask(__name__)

# @flask_app.route('/')
# def homepage():
#     return 'This is the home page. Nothing here, really.'

app = FastAPI() 

router = APIRouter()


@router.get('/colors', response_model=List[schema.Color])
def get_all():
    return db.get_all_colors()


@router.post('/colors', response_model=schema.Color)
def add_new_color(color: schema.ColorCreate):
    return db.add_color(color)
    

@router.delete('/admin_color_delete', status_code=200)
def delete_all():
    db.delete_all_colors()
    return {'success': 'Deleted all favorite colors'}


app.include_router(router, prefix='/api', tags=['colors'])


# # https://docs.python.org/3/library/typing.html#typing.Union
# @app.get('/colors/{color_id}')
# # The query param can be the type string or None; Union allows defining it to be one or the other
# def read_color(color_id: int, thing: Union[str, None] = None):
#     return {'color_id': 12345, 'you_asked': thing}

"""
This request 
http://127.0.0.1:8000/colors/2?thing=stuff

returns 

{
"color_id": 12345,
"you_asked": "stuff"
}


And there's documentation at http://127.0.0.1:8000/docs
"""