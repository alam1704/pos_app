from flask import Blueprint, request, redirect, abort, url_for, send_from_directory
from pathlib import Path
from models.dish import Dish
import os

dish_images = Blueprint('dish_images', __name__)

@dish_images.route("/dishes/<int:id>/image/", methods=["POST"])
def update_image(id):
    dish=Dish.query.get_or_404(id)
    if "image" in request.files:
        image=request.files["image"]

        file_types=[".jpg",".jpeg", ".png",".gif",".tiff",".psd",".pdf",".eps",".ai",".indd",".raw"]
        for file_type in file_types:
            if Path(image.filename).suffix != file_type:
                return abort(400, description="Invalid File Type")
            image.save(f"pos_app/static/{dish.dish_image}")
            return redirect(url_for("dishes.item_retrieve", id=id))
    return abort(400, description="No Image")