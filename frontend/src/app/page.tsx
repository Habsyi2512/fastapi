async function getData() {
  const response = await fetch("http://localhost:8000/api");
  const data = await response.json();
  return data;
}

export default async function Home() {
  const data = await getData();
  return (
    <div>
      <h1>Halaman Utama</h1>
      <p>{data.Hello}</p>
    </div>
  );
}
