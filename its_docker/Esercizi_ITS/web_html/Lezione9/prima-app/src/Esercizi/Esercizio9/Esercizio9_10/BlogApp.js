import React, { useState } from 'react'
import PostForm from './PostForm'
import PostList from './PostList'

const BlogApp = () => {

    const [posts, setPosts] = useState([])

    const aggiungiPosts = (post) => {

        setPosts(prevPosts => [

            ...prevPosts, post

        ])
    }

    return (

        <div>

            <PostForm aggiungiPosts={aggiungiPosts}/>
            <PostList posts={posts}/>
            
        </div>
    )
}

export default BlogApp