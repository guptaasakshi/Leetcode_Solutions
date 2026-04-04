var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    
    const exists = this.cache.has(key) && this.cache.get(key).expiry > now;

    this.cache.set(key, {
        value: value,
        expiry: now + duration
    });

    return exists;
};

TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();

    if (!this.cache.has(key)) return -1;

    const entry = this.cache.get(key);

    if (entry.expiry < now) return -1;

    return entry.value;
};

TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;

    for (let [key, entry] of this.cache) {
        if (entry.expiry > now) {
            count++;
        }
    }

    return count;
};