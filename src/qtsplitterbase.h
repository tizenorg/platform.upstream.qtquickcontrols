#ifndef QTSPLITTERBASE_H
#define QTSPLITTERBASE_H

#import <QtDeclarative>


class QtSplitterAttached : public QObject
{
    Q_OBJECT
    Q_PROPERTY(qreal minimumSize READ minimumSize WRITE setMinimumSize NOTIFY minimumSizeChanged)
    Q_PROPERTY(qreal maximumSize READ maximumSize WRITE setMaximumSize NOTIFY maximumSizeChanged)
    Q_PROPERTY(qreal percentageSize READ percentageSize WRITE setPercentageSize NOTIFY percentageWidthSize)
    Q_PROPERTY(bool expanding READ expanding WRITE setExpanding NOTIFY expandingChanged)
    Q_PROPERTY(int itemIndex READ itemIndex WRITE setItemIndex NOTIFY itemIndexChanged)

public:
    explicit QtSplitterAttached(QObject *object);

    qreal minimumSize() const { return m_minimumSize; }
    void setMinimumSize(qreal width);

    qreal maximumSize() const { return m_maximumSize; }
    void setMaximumSize(qreal width);

    bool expanding() const { return m_expanding; }
    void setExpanding(bool expanding);

    qreal percentageSize() const { return m_percentageSize; }

    int itemIndex() const { return m_itemIndex; }

    void setPercentageSize(qreal arg) { m_percentageSize = arg; }
    void setItemIndex(int arg) {
        if (m_itemIndex != arg) {
            m_itemIndex = arg;
            emit itemIndexChanged(arg);
        }
    }

signals:
    void minimumSizeChanged(qreal arg);
    void expandingChanged(bool arg);
    void percentageWidthSize(qreal arg);
    void maximumHeight(qreal arg);
    void maximumSizeChanged(qreal arg);
    void minimumHeightChanged(qreal arg);
    void itemIndexChanged(int arg);

private:
    qreal m_minimumSize;
    qreal m_maximumSize;
    qreal m_percentageSize;
    int m_itemIndex;
    bool m_expanding;

    friend class QtSplitterBase;
};


class QtSplitterBase : public QDeclarativeItem
{
    Q_OBJECT
public:
    explicit QtSplitterBase(QDeclarativeItem *parent = 0);
    ~QtSplitterBase() {}

    static QtSplitterAttached *qmlAttachedProperties(QObject *object);
};

QML_DECLARE_TYPEINFO(QtSplitterBase, QML_HAS_ATTACHED_PROPERTIES)

#endif // QTSPLITTERBASE_H