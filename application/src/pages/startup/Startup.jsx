import { Link } from "react-router-dom";
import "./startup.css";
import Card from "../../common/Card";
import '../../common/global.css'; // Import the global CSS

import image1 from "../../assets/ph.jpg";
import image2 from "../../assets/water.jpg";
import image3 from "../../assets/water2.jpg";
import chlorine from "../../assets/chlorine.png";
import odor from "../../assets/odor.png";
import iron from "../../assets/iron.jpeg";
import nitrate from "../../assets/nitrate.png";
import chloride from "../../assets/chloride.png";
import color from "../../assets/color.png";
import turbidity from "../../assets/turbidity.jpg";
import floride from "../../assets/floride.png";
import copper from "../../assets/copper.jpg";
import sulphate from "../../assets/sulphate.jpg";
import manganese from "../../assets/manganese.jpeg";
import tds from "../../assets/tds.jpeg";
import watertemp from "../../assets/watertemp.png";
import airtemp from "../../assets/airtemp.jpeg";

const cards = [
  {
    id: 1,
    title: "pH",
    image: image1,
    paragraph: "The pH of most drinking-water lies within the range 6.5–8.5.Natural waters can be of lower pH, as a result of, for example, acid rain or higher pH in limestone areas."
  },
  {
    id: 2,
    title: "Iron",
    image: iron,
    paragraph: "Water with an iron level above 0.3 milligrams per liter (mg/L) is usually considered objectionable. Iron levels are usually below 10 mg/L in water.",
  },
  {
    id: 3,
    title: "Nitrate",
    image: nitrate,
    paragraph: "Drinking water with levels of nitrate at or below 10 mg/L is considered safe for everyone.Nitrate levels above the Maximum Contaminant Level may cause methemoglobinemia in infants.",
  },
  {
    id: 4,
    title: "Chloride",
    image: chloride,
    paragraph: "The recommended limit for chlorides is 250 milligrams per liter (mg/1). This is the concentration in water where most people will notice a salty taste.",
  },
  {
    id: 5,
    title: "Color",
    image: color,
    paragraph: "However, the color of drinking water can sometimes be affected by various factors, including the presence of natural minerals, sediments, or contaminants.",
  },
  {
    id: 6,
    title: "Turbidity",
    image: turbidity,
    paragraph: "Turbidity is the measure of relative clarity of a liquid. Turbidity of drinking water shouldn't be more than 5 NTU, and should ideally be below 1 NTU.",
  },
  {
    id: 7,
    title: "Fluoride",
    image: floride,
    paragraph: "According to World Health Organization, standard rate of fluoride of drinking water is 0.5–1 ppm.",
  },
  {
    id: 8,
    title: "Copper",
    image: copper,
    paragraph: "A provisional drinking-water guideline of 2 mg/L was proposed for copper by the World Health Organization",
  },
  {
    id: 9,
    title: "Odor",
    image: odor,
    paragraph: "The reported odour threshold in water ranges from 2 to 130 μg/l. The lowest reported odour threshold is 100-fold lower than the health-based guideline value of 0.3 mg/l .",
  },
  {
    id: 10,
    title: "sulphate",
    image: sulphate,
    paragraph: "Sulfate in drinking water currently has a secondary maximum contaminant level (SMCL) of 250 milligrams per liter (mg/L), based on aesthetic effects.",
  },
  {
    id: 11,
    title: "Conductivity",
    image: image3,
    paragraph: "Conductivity ranges between water bodies, but typically lakes and streams have a conductivity range between 0-200 µS/cm, while major rivers can have a conductance value up to 1000 µS/cm.",
  },
  {
    id: 12,
    title: "Chlorine",
    image: chlorine,
    paragraph: "Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water . At this level, harmful health effects are unlikely to occur.",
  },
  {
    id: 13,
    title: "Manganese",
    image: manganese,
    paragraph: "US EPA) has developed a health advisory level for manganese in drinking water of 0.3 mg/L and a secondary drinking water guideline of 0.05 mg/L for aesthetic issues.",
  },
  {
    id: 14,
    title: "Total Dissolved Solids",
    image: tds,
    paragraph: "the total concentration of dissolved substances in water. The normal TDS level ranges from 50 ppm to 1,000 ppm. ",
  },
  {
    id: 15,
    title: "Water Temperature",
    image: watertemp,
    paragraph: "The best temperature for drinking water is room temperature (20°C / 68°F) for maximum flavour, or chilled cold (6°C / 43°F) for maximum refreshment.",
  },
  {
    id: 16,
    title: "Air Temperature",
    image: airtemp,
    paragraph: "The air temperature does not directly affect the safety or quality of drinking water. ",
  },
];

function Startup() {
  document.title = "FDM | Startup";

  // Calculate the number of columns for a 4-card grid
  const numColumns = 4;

  // Split the cards into groups of 4 for each row
  const rows = [];
  for (let i = 0; i < cards.length; i += numColumns) {
    rows.push(cards.slice(i, i + numColumns));
  }

  return (
    <>
      <div className="container">
        {rows.map((row, rowIndex) => (
          <div className="row" key={rowIndex}>
            {row.map(({ title, image, paragraph, id }) => (
              <div className={`col-md-${12 / numColumns}`} key={id}>
                <Card imageSource={image} title={title} text={paragraph} />
              </div>
            ))}
          </div>
        ))}
      </div>
    </>
  );
}

export default Startup;

