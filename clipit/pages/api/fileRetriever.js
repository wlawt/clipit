// source: https://stackoverflow.com/questions/15696218/get-the-most-recent-file-in-a-directory-node-js

const fs = require('fs');
const path = require('path');
const _ = require('underscore');

const getRecentClip = dir => {
  var files = fs.readdirSync(dir);

  // use underscore for max()
  return _.max(files, function (f) {
    var fullpath = path.join(dir, f);

    // ctime = creation time is used
    // replace with mtime for modification time
    return fs.statSync(fullpath).ctime;
  });
}

export default (req, res) => {
  res.status(200).json(getRecentClip("D:/CodingFolder/clipit/clipit/clips/"))
}