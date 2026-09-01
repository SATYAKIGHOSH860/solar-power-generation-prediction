# ☀️ Solar Power Generation Prediction

Machine learning system that predicts the **DC power output** of a solar power plant from
weather sensor readings and recent generation history.

**🔗 Live app:** https://solar-power-generation-prediction-ml.streamlit.app/

---

## Project Overview

The model is trained on historical **solar generation data** and **weather sensor data** from two
solar plants, and is deployed as an interactive **Streamlit web application** for real-time
predictions.

The goal is to estimate solar power generation from environmental and operational parameters,
supporting better energy planning and grid scheduling.

---

## Machine Learning Approach

- **Algorithm:** Random Forest Regressor
- **Type:** Supervised regression
- **Target variable:** `DC_POWER`

### Input Features

The deployed model uses five features:

| Feature | Description |
|---|---|
| `IRRADIATION` | Solar irradiation from the weather sensor |
| `MODULE_TEMPERATURE` | Panel surface temperature (°C) |
| `DC_lag_1` | DC power one interval ago (15 minutes) |
| `DC_roll_3` | Rolling mean of the last three DC readings (45 minutes) |
| `DC_lag_24` | DC power 24 intervals ago (6 hours) |

The lag and rolling features come from time-series feature engineering on 15-minute interval
sensor data. Ambient temperature and daily yield were explored during analysis but are not part
of the final feature set.

---

## Results

Five regression models were compared under two different evaluation strategies.

**Random split** — rows shuffled before splitting:

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Extra Trees | 24.69 | 104.83 | 0.999 |
| **Random Forest** | **26.24** | **132.47** | **0.998** |
| Gradient Boosting | 74.32 | 159.77 | 0.998 |
| ANN (MLP) | 67.46 | 200.97 | 0.996 |
| Linear Regression | 188.86 | 479.37 | 0.980 |

**Time-based split** — trained on earlier data, tested on later data:

| Model | MAE | RMSE | R² |
|---|---|---|---|
| **Random Forest** | **26.16** | **114.70** | **0.877** |
| Extra Trees | 28.36 | 115.87 | 0.875 |
| ANN (MLP) | 38.71 | 116.08 | 0.874 |
| Gradient Boosting | 46.49 | 119.20 | 0.868 |

### Why both splits were evaluated

A random split lets the model train on readings that occur *after* the ones it is tested on. For
a forecasting problem that is unrealistic, since production always means predicting forward in
time. The time-based split is the more honest estimate of deployment performance.

Note that R² falls sharply between the two (0.998 to 0.877) while RMSE stays similar and actually
improves slightly (132.47 to 114.70). This is because the two evaluations use different test sets
with different variance — R² is scaled by the variance of the data being predicted, so it is not
directly comparable across splits. **RMSE is the metric to compare here**, and by that measure
Random Forest performs consistently under both strategies.

Random Forest was selected for deployment: it was the best or near-best model under both splits
and the most stable between them.

---

## Project Structure

```
solar-power-generation-prediction/
│
├── app.py                  # Streamlit web application
├── requirements.txt
├── README.md
├── LICENSE
│
├── model/
│   └── solar_rf_small.pkl  # Trained Random Forest
│
└── notebooks/
    └── solar_power_gen_project.ipynb
```

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib, Seaborn
- Git & GitHub

---

## Dataset

Solar Power Generation Data — Plant 1 and Plant 2, each with a generation file and a weather
sensor file, recorded at 15-minute intervals.

Source: [Kaggle — Solar Power Generation Data](https://www.kaggle.com/datasets/anikannal/solar-power-generation-data)

The CSV files are not committed to this repository due to size.

---

## Running Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

The application opens automatically in your browser.

---

## Pipeline

1. **Load and merge** generation and weather sensor data on timestamp and plant ID
2. **Clean** — remove night-time zero-generation rows and sensor anomalies via Isolation Forest
3. **Feature engineering** — lag features (`DC_lag_1`, `DC_lag_24`), rolling means (`DC_roll_3`),
   and irradiation rolling windows from the time-series
4. **Train and compare** five regression models under both split strategies
5. **Persist** the final Random Forest with `joblib`
6. **Deploy** via Streamlit Community Cloud

---

## Deployment Notes

The saved artifact stores the feature names it was trained on. The Streamlit app passes inputs as
a **pandas DataFrame with named columns** rather than a raw NumPy array, so scikit-learn validates
feature names and order at prediction time.

This matters: with a bare NumPy array, scikit-learn accepts any five numbers in any order and
returns a plausible-looking but incorrect prediction. Passing a named DataFrame turns a silent
failure into an explicit error.

---

## Limitations

- Trained on two plants over a 34-day period; generalisation to other sites is untested
- The model requires recent DC power history, so it cannot cold-start without prior readings
- Evaluated on a single time-based split rather than a rolling-origin backtest
- No live sensor integration — inputs are entered manually in the app

---

## Possible Extensions

- Walk-forward (rolling-origin) validation for a more robust temporal estimate
- Multi-horizon forecasting (predict 1 hour and 24 hours ahead)
- Direct weather API integration for automated inputs
- Per-inverter modelling rather than plant-level aggregation

---

## Author

**Satyaki Ghosh** — M.Tech, Artificial Intelligence & Data Science, KIIT Bhubaneswar

[GitHub](https://github.com/SATYAKIGHOSH860)
