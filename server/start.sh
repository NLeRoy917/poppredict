#! bin/bash
source ../env/bin/activate
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=serve
python -m flask run