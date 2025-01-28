import React from "react";

const Footer = () => {
  return (
    <footer className="bg-light text-center text-secondary py-3 mt-5">
      <p style={{ marginBottom: 0 }}>
        &copy; {new Date().getFullYear()} Gender Inequality in Economics PhD. 
        Created by Lea, Samantha, Amy, Chris, and Tracy.
      </p>
    </footer>
  );
};

export default Footer;
