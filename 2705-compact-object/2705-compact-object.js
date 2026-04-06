var compactObject = function(obj) {
    // base case
    if (obj === null) return null;

    // array case
    if (Array.isArray(obj)) {
        return obj
            .filter(Boolean)
            .map(item => compactObject(item));
    }

    // object case
    if (typeof obj === "object") {
        let result = {};

        for (let key in obj) {
            const value = compactObject(obj[key]);

            if (Boolean(value)) {
                result[key] = value;
            }
        }

        return result;
    }

    return obj;
};