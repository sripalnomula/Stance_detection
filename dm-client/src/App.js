import { Route, Routes } from "react-router-dom"
import './App.css';
import Navbar from "./Components/Navbar/navbar";
import Home from "./Components/Home/home";
import AboutApi from "./Components/aboutApi/aboutApi";
import Footer from "./Components/Footer/footer";
// import bg from "@/public/news_bg.jpeg"
function App() {
  return (
    <>
    <div>
      <Navbar />
        <div className="container">
          <Routes>
            <Route path="/" element={<Home />} />
            {/* <Route path="/pricing" element={<Pricing />} /> */}
            <Route path="/about-api" element={<AboutApi />} />
          </Routes>
        </div>
      <Footer/>
    </div>
      
    </>
  );
}

export default App;
