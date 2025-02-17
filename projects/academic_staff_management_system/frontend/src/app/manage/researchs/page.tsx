import ManagerHeader from "../../components/ManagerHeader";
import ManageMenu from "../../components/ManageMenu";
import ResearchForm from "@/app/components/ResearchForm";

const page = () => {
  return (
    <div className="bg-main-white min-h-screen flex flex-col">
      <ManagerHeader />
      <div className="flex">
        <ManageMenu />
        <div>
          <form action="" method="">
            <ResearchForm></ResearchForm>
          </form>
        </div>
      </div>
    </div>
  );
};

export default page;
