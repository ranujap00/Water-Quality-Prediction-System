import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Startup from "../pages/startup/Startup";
import Navbar from "../common/Navbar"
import TestWaterPotability from '../pages/testWaterPotability/TestWaterPotability'

function AppRoutes() {
  return (
    <Router>
      <Navbar/>
      <Routes>
        <Route path="/" element={<Startup />} />
        <Route path="/waterPotability" element={<TestWaterPotability />} />
      </Routes>
    </Router>
  );
}
export default AppRoutes;