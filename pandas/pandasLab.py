# -*- coding: utf-8 -*-
import numpy
import pandas

DAYS_TO_YEAR_COEF = 0.00273973
DAYS_TO_MONTH_COEF = 0.03287672397071
CENTIMETER_TO_METER_COEF = 0.01

pandas.set_option('precision', 4)

def is_bmi_normal(bmi):
    return bmi >= 18.5 and bmi <= 25

def get_cholesterol(mmol_per_liter):
    return {
        4: 1,
        5: 2,
        6: 2,
        7: 2,
        8: 3
    }[mmol_per_liter]

data = pandas.read_csv("data.csv", sep=";", index_col="id")

# Task #1

gender_height_mean = data.groupby(["gender"])["height"].mean()
data["gender"] = data["gender"].map({
gender_height_mean.idxmax(): "male",
    gender_height_mean.idxmin(): "female"
})
gender_value_counts = data["gender"].value_counts().to_dict()

print("Кількість чоловіків: {}".format(gender_value_counts["male"]))
print("Кількість жінок: {}".format(gender_value_counts["female"]))
print("\n")

# Task #2

gender_alco_dict = data.groupby(["gender"])["alco"].mean().to_dict()
print("{:.0%} чоловіків вживають алкоголь".format(gender_alco_dict["male"]))
print("{:.0%} жінок вживають алкоголь".format(gender_alco_dict["female"]))
print("\n")

# Task #3

gender_smoke_mean = data.groupby(["gender"])["smoke"].mean()
print("Відсоток курців серед чоловіків у {:.2f} рази більший, ніж відсоток курців серед жінок".format(
    gender_smoke_mean["male"] / gender_smoke_mean["female"]))
print("\n")

# Task #4

smoke_age_median = data.groupby(["smoke"])["age"].median() * DAYS_TO_MONTH_COEF
print("Середній вік курців в місяцях {:.2f}".format(smoke_age_median[1]))
print("Середній вік не курящих людей в місяцях {:.2f}".format(smoke_age_median[0]))
print("Різниця між ними {:.2f}".format(smoke_age_median[1] - smoke_age_median[0]))
print("\n")


# Task #6

data["bmi"] = data["weight"] / \
    ((data["height"] * CENTIMETER_TO_METER_COEF) ** 2)

median_bmi = data["bmi"].median()
print("1: Середій BMI {:.2f} по вибірці перевищує норму - {}.".format(
    median_bmi,
    not is_bmi_normal(median_bmi)
))

mean_gender_bmi = data.groupby(["gender"])["bmi"].mean()
print("2: Середній BMI у чоловіків - {:.2f}, середній BMI у жінок - {:.2f}.".format(
    mean_gender_bmi["male"],
    mean_gender_bmi["female"]
))

cardio_bmi_mean = data.groupby(["cardio"])["bmi"].mean()
print("3: Середій BMI у хворих людей - {:.2f}, середній BMI у здорових людей - {:.2f}.".format(
    cardio_bmi_mean[1],
    cardio_bmi_mean[0]
))

mean_bmi_for_healthy_people = data[
    (data["alco"] == 0) &
    (data["cardio"] == 0)
].groupby(["gender"])["bmi"].mean()

print("4: Середній BMI у здорових чоловіків - {:.2f}, середній BMI у здорових жінок - {:.2f}.".format(
    mean_bmi_for_healthy_people["male"],
    mean_bmi_for_healthy_people["female"]
))
print("\n")

# Task #7

quantiles = [.025, .975]
height_quantiles = data["height"].quantile(quantiles)
weight_quantiles = data["weight"].quantile(quantiles)

records_to_remove = data[
    (data["weight"] < weight_quantiles[quantiles[0]]) |
    (data["weight"] > weight_quantiles[quantiles[1]]) |
    (data["height"] < height_quantiles[quantiles[0]]) |
    (data["height"] > height_quantiles[quantiles[1]]) |
    (data["ap_lo"] > data["ap_hi"])
]

print("{:.1%} даних ми викинули".format(records_to_remove.shape[0] / data.shape[0]))