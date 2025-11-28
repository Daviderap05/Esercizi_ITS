import React, { useState, useEffect } from "react";

const PostsGrid = () => {
  const [post, setPost] = useState([]);

  const urlPosts = "https://jsonplaceholder.typicode.com/posts/";
  const urlUsers = "https://jsonplaceholder.typicode.com/users/";
  const urlCommenti = "https://jsonplaceholder.typicode.com/comments/";

  async function fetchDetailsPosts(post) {
    const userP = fetch(urlUsers + post.userId).then((resp) => resp.json());
    const commentiP = fetch(urlCommenti + "?postId=" + post.id).then((resp) =>
      resp.json()
    );

    const [user, comments] = await Promise.all([userP, commentiP]);

    return {
      ...post,
      user: user.name,
      comments,
    };
  }

  const fetchPost = async () => {
    try {
      const response = await fetch(urlPosts);
      if (!response.ok) {
        throw new Error("Errore nella chiamata a " + urlPosts);
      }

      const allPosts = await response.json();

      //con parentesi tonde il return è implicito
      const allDataPromise = allPosts.map((post) => {
        return fetchDetailsPosts(post);
      });

      const allData = await Promise.all(allDataPromise);
      setPost(allData);
    } catch (err) {
      console.log(err.message);
    }
  };

  useEffect(() => {
    // chiama la funzione quando il componente monta
    fetchPost();
  }, []);

  return (
    <div style={styles.container}>
      {post.map((p) => (
        <div style={styles.card} key={p.id}>
          <h2 style={styles.h2}>{p.title}</h2>
          <p style={styles.p}>{p.body}</p>
          <small style={styles.small}>{p.user}</small>
          <ul style={styles.ul}>
            {p.comments.map((c) => (
              <li style={styles.li} key={c.id}>
                {c.name}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexWrap: "wrap",
    gap: "20px",
    justifyContent: "center",
  },

  card: {
    backgroundColor: "white",
    border: "1px solid #c9c9c9",
    padding: "20px",
    borderRadius: "15px",
    maxWidth: "350px",
    boxShadow: "0 4px 8px rgb(0, 0, 0, 0.1)",
  },

  ul: {
    listStyleType: "none",
    paddingLeft: "0",
  },

  li: {
    margin: "5px 0",
    padding: "2px 0",
  },

  p: {
    fontSize: "0.8rem",
  },

  h2: {
    fontSize: "1.4rem",
  },

  small: {
    color: "cornflowerblue",
    fontWeight: "700",
  },
};

export default PostsGrid;
