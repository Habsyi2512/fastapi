type Profile = {
  nama: string;
  umur: number;
  pekerjaan: string;
};

async function getProfile(): Promise<Profile> {
  const response = await fetch("http://localhost:8000/api/get-profile");
  const data = await response.json();
  return data;
}

export default async function Home() {
  const dataProfile = await getProfile();
  return (
    <div className="w-full">
      <h1 className="text-2xl text-center py-8 text-neutral-700 font-bold">Halaman Utama</h1>
      <div className="w-full max-w-xl p-2 shadow rounded mx-auto bg-neutral-300">
        <p>nama : {dataProfile.nama}</p>
        <p>umur : {dataProfile.umur}</p>
        <p>pekerjaan : {dataProfile.pekerjaan}</p>
      </div>
    </div>
  );
}
