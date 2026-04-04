var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        const results = [];
        let completed = 0;

        if (functions.length === 0) {
            resolve([]);
        }

        functions.forEach((fn, index) => {
            fn()
                .then((res) => {
                    results[index] = res; // order maintain
                    completed++;

                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch((err) => {
                    reject(err); // fail fast
                });
        });
    });
};