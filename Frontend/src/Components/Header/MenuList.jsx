import { motion } from "framer-motion";

const MenuList = ({ isOpen }) => {
  return (
    <motion.article
      className="menu-list"
      animate={{
        height: isOpen ? "auto" : "0rem",
        marginTop: isOpen ? "1em" : "0em",
      }}
      initial={{
        height: "0rem",
        marginTop: "0rem",
      }}
      transition={{
        type: "spring",
        stiffness: 60,
        duration: 5,
      }}
    >
      <ul className="menu-list-items">
        <li>
          <h3>Home</h3>
        </li>
        <li>
          <h3>Add Food</h3>
        </li>
        <li>
          <h3>Food Diary</h3>
        </li>
        <li>
          <h3>Summary</h3>
        </li>
        <li>
          <h3>Setting</h3>
        </li>
      </ul>
    </motion.article>
  );
};
export default MenuList;
