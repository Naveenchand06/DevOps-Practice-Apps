import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [data1, setData1] = useState(null);

  useEffect(() => {
    axios.get(`${import.meta.env.VITE_API_BASE_URL}/data1`)
      .then(res => setData1(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>Home Page</h2>
      <pre>{JSON.stringify(data1, null, 2)}</pre>
    </div>
  );
}