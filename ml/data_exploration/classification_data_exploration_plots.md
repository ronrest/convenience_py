## Distribution of Features for Classification Task

View distribution of each of the features as a kernel density estimation plot, split by the class.

![](kde_features.jpg)

```py
n_features = len(features)
f, axes = plt.subplots(n_features, 2, figsize=(10, 100), sharex=True, sharey=False)
#axes = np.array(axes).flatten() # Unroll axes to a flat list
for row in range(len(axes)):
    # LEFT SIDE
    ax = axes[row][0]
    ax = sns.kdeplot(df.iloc[ones,row], shade=True, color="r", ax=ax)
    ax = sns.kdeplot(df.iloc[np.invert(ones),row], shade=True, color="b", ax=ax)
    ax.set_xlim([0, 1])

    # RIGHT SIDE
    ax = axes[row][1]
    ax = sns.regplot(x=df.iloc[:,row], y=np.array(df["target"]), ax=ax)
    ax.set_aspect(0.3, "box-forced")
```
