
# Compressive strength of concrete prediction

This project is a regression problem exicuted using XGBoost regressor in Python language.The purpose of this project is to creat a model which can predict compressive strength value corresponding to given ingridients volume used for prepairing a concrete mix.

Concrete is the most important material in civil engineering. The
concrete compressive strength is a highly nonlinear function of age and
ingredients. These ingredients include cement, blast furnace slag, fly ash,
water, superplasticizer, coarse aggregate, and fine aggregate.


## 🚀 About Me
I'm a beginer in Data science.I have done my graduation in Civil engineering.


## Acknowledgements

 - [compressive strength of the concrete cube test procudere ](https://theconstructor.org/concrete/compressive-strength-concrete-cube-test/1561/)



## Data

[Data is taken from kaggle](https://www.kaggle.com/elikplim/concrete-compressive-strength-data-set).
## Data Characteristics:

The actual concrete compressive strength (MPa) for a given mixture under a
specific age (days) was determined from laboratory. Data is in raw form (not scaled).

## Summary Statistics:

- Number of instances (observations): 1030
- Number of Attributes: 9
- Attribute breakdown: 8 quantitative input variables, and 1 quantitative output variable
- Missing Attribute Values: None
## Lessons Learned

- Dataset has no missing values
- Compressive strength of concrete is highly correlated with cement,water,superplasticizer and age of concrete.
- Water is highly negatively correlated with superplasticizer.It means that superplasticizer provides flexiblity to use less water because more water results in reduced compressive strength.
- Replacing the outliers by median


## Final observation

- Among all the six different algorithms,XGBoost Regressor gives the best result.So,we will use XGBoost model for deployment
## Deployment

App is prepaired using streamlit libraray.
To run this app in local default browsser,type bellow command in terminal

```bash
  streamlit run app.py
```
[App was finally diployed on Heroku pltform](https://compressivestrengthofconcrete.herokuapp.com/).



## License

[MIT](LICENSE.txt)


## Demo

To see this herokuapp running live,click bellow

https://compressivestrengthofconcrete.herokuapp.com/
## Badges



[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Chetankumar71297/Compressive-strength-of-concrete/blob/master/LICENSE.txt)

