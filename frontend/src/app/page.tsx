import AddUserForm from "@/components/form/AddUserForm";

export default async function Home() {
  return (
    <div className="w-full">
      <h1 className="text-2xl text-center py-8 text-neutral-700 font-bold">
        Halaman Utama
      </h1>
      <div className="w-full max-w-xl p-2 shadow rounded mx-auto bg-neutral-300">
        <p className="text-xl text-center">Ini adalah contoh halaman utama.</p>
        <AddUserForm />
      </div>
    </div>
  );
}
