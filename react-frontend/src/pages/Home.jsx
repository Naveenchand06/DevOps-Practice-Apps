import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [isLoading, setLoading] = useState(false);
  const [data1, setData1] = useState(null);

  useEffect(() => {
    setLoading(true);
    axios.get(`${import.meta.env.VITE_API_BASE_URL}/data1`)
      .then(res => setData1(res.data))
      .catch(err => console.error(err));
    setLoading(false);
  }, []);

  return (
    <div>
      <h2>Home Page</h2>
      {isLoading ? "Loading..." :  <pre>{JSON.stringify(data1, null, 2)}</pre>}
    </div>
  );
}