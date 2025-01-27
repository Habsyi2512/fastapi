import AddUserForm from "@/components/form/AddUserForm";

export default async function Home() {
  return (
    <div className="w-full">
      <h1 className="text-2xl text-center py-8 text-neutral-700 font-bold">
        Halaman Utama
      </h1>
      <div className="w-full max-w-xl p-2 shadow rounded mx-auto bg-neutral-300">
        <h1 className="text-center py-5 text-2xl font-bold text-neutral-700">Form</h1>
        <AddUserForm />
      </div>
    </div>
  );
}
