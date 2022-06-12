const translation ={
    en: {
        textUpper : "We are here to help you achieve your goals",
		about : "about"
    },
    ar: {
        textUpper : "نحن هنا لخدمتك",
		about: "بشان"

    }
};

const LanguageSelector = document.querySelector("select");
// console.log(LanguageSelector);
LanguageSelector.addEventListener("change", (event) =>{
    setLanguage(event.target.value);
});

const setLanguage = (language) => {
    const elements = document.querySelectorAll("[data-il8n]");
    elements.forEach((element) =>{
        const translationKey = element.getAttribute("data-il8n");
        element.textContent = translation[language][translationKey];
    });

};