var join = function(arr1, arr2) {
    const map = {};

    // step 1: add arr1
    for (let obj of arr1) {
        map[obj.id] = obj;
    }

    // step 2: merge arr2
    for (let obj of arr2) {
        if (map[obj.id]) {
            map[obj.id] = { ...map[obj.id], ...obj };
        } else {
            map[obj.id] = obj;
        }
    }

    // step 3: return sorted result
    return Object.values(map).sort((a, b) => a.id - b.id);
};