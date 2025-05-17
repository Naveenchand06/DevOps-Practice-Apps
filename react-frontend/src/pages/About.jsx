import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function About() {
  const [data2, setData2] = useState(null);

  useEffect(() => {
    axios.get(`${import.meta.env.API_BASE_URL}/data2`)
      .then(res => setData2(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2>About Page</h2>
      <pre>{JSON.stringify(data2, null, 2)}</pre>
    </div>
  );
}