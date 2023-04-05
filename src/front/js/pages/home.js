import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/pages/home.css";

import fit_00 from "../../img/home/AdobeStock4.jpeg";
import fit_01 from "../../img/home/AdobeStock2.jpeg";
import fit_02 from "../../img/home/AdobeStock3.jpeg";
import fit_03 from "../../img/home/AdobeStock1.jpeg";

import Hero from "../component/hero.js";
import Slider from "../component/slider.js";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="App">
			<Hero imageSrc={fit_03} />
			<Slider
				imageSrc={fit_01}
				title={"Achieve Your Fitness Goals"}
				subtitle={"This is your Ultimate Guide to Health and Wellness!"}
			/>
			<Slider
				imageSrc={fit_00}
				title={"Start your Journey Today!"}
				subtitle={
				"Join to Our Fitness Community and Transform your Body and Mind."
				}
				flipped={true}
			/>
			{/* <video autoPlay loop muted>
				<source src={video} type="video/mp4" />
			</video> */}
	  	</div>
	);
};
