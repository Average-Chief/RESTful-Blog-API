from flask import Flask, request, jsonify
from httpx import post
from sqlmodel import select
from datetime import datetime

from database.db import create_db, get_session
from models.models import BlogPost
from schema import BlogPostCreate, BlogPostUpdate

app= Flask(__name__)
create_db()

#create a blog post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    try:
        payload=BlogPostCreate(**data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    post = BlogPost(**payload.dict(),created_at=datetime.utcnow(), updated_at=datetime.utcnow())

    with get_session() as session:
        session.add(post)
        session.commit()
        session.refresh(post)

    return jsonify(post.dict()), 201

#update a blog post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.get_json()

    try:
        payload = BlogPostUpdate(**data)
    except Exception as e:
        return jsonify({"error":str(e)}), 400
    
    with get_session() as session:
        post = session.get(BlogPost, post_id)

        if not post:
            return jsonify({"error":"Post not found"}), 404
        
        for key, value in payload.dict().items():
            setattr(post,key,value)

        post.updated_at = datetime.utcnow()

        session.add(post)
        session.commit()
        session.refresh(post)

    return jsonify(post.dict()), 200

#delete a blog post
@app.route('/posts/<int:post_id>', methods = ['DELETE'])
def delete_post(post_id):
    with get_session() as session:
        post = session.get(BlogPost, post_id)

        if not post:
            return jsonify({"error":"Post not found"}), 404
        
        session.delete(post)
        session.commit()

    return "",204

#get a single blog post
@app.route('/posts/<int:post_id>', methods = ['GET'])
def get_post(post_id):
    with get_session() as session:
        post = session.get(BlogPost, post_id)

        if not post:
            return jsonify({"error":"Post not found"}), 404
        
    return jsonify(post.dict()),200

#get all blog posts with optional search
@app.route('/posts', methods = ['GET'])
def get_all_post():
    term = request.args.get('term')
    with get_session() as session:
        query = select(BlogPost)

        if term:
            like_term = f"%{term.lower()}%"
            query = query.where(
                (BlogPost.title.ilike(like_term)) |
                (BlogPost.content.ilike(like_term)) |
                (BlogPost.category.ilike(like_term)) 
            )
        
        posts = session.exec(query).all()

        
    return jsonify([post.dict() for post in posts]), 200

if __name__ == '__main__':
    app.run(debug=True)
