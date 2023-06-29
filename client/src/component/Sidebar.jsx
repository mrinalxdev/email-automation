import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { logo, sun } from "../assets";
import { navlinks } from "../constants";

const Icon = ({ styles, name, imgUrl, isActive, disabled, handleClick }) => (
  <div
    className={`w-[48] h-[48px] rounded-[20px] ${
      isActive && isActive === name && "bg-[#2c2f32]"
    } flex justify-center items-center ${!disabled && "cursor-pointer"} ${styles}`} onClick={handleClick}
  >
    {isActive ? (
      <img src={imgUrl} className="w-1/2 h-1/2" />
    ) : (
      <img src={imgUrl} className={`w-1/2 h-1/2 ${isActive !== name && 'grayscale'}`} />
    ) }
  </div>
);

const Sidebar = () => {
  const navigate = useNavigate();
  const [isDark, setIsDark] = useState(false);
  const [isActive, setIsActive] = useState("dashboard");
  return (
    <div className="flex justify-between items-center flex-col sticky top-5 h-[93vh]">
      {/* Home Redirection */}
      <Link to="/">
        <Icon styles="w-[52px] h-[52px] bg-[#2c2f32]" imgUrl={logo} />
      </Link>
    </div>
  );
};

export default Sidebar;
